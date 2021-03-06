ifndef message
	message = "Updating web app"
endif

ifndef repos
	repos = mlhamel/atelierlaurier
endif

ifndef revision
	tag = latest
endif

.SHELLFLAGS = -e
.PHONY: docker-build
.NOTPARALLEL:

default: build
build: docker-build
commit: docker-commit
push: docker-push
tag: docker-tag
docker-build: do-docker-build
docker-commit: do-docker-commit
docker-push: do-docker-push
docker-tag: do-docker-tag

do-docker-build:
	docker build -t atelierlaurier --no-cache --rm . | tee build.log || exit 1

do-docker-commit:
	docker commit -m $(message) $(revision) $(repos)

do-docker-push:
	docker push $(repos):$(tag)

do-docker-tag:
	docker tag -f $(revision) $(repos)

# Version Bump using bumpversion
patch:
	bumpversion patch
major:
	bumpversion major
minor:
	bumpversion minor

run:
	pserve development.ini
