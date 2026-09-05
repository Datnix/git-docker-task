Why should generated files, virtual environments, secrets, and raw/private datasets not necessarily be committed to Git?

answer:
   We don't commit these files because they can be generated again may be too large or may contain private data like passwords, API keys, or raw datasets.

------------------------------------------------------------------

Dockerfile vs Image vs Container

-Dockerfile: A file with instructions to build the Docker image.
-Image: A ready package that contains the app and everything it needs.
-Container: A running instance of the image.

------------------------------------------------------------------