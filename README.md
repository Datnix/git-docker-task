Why should generated files, virtual environments, secrets, and raw/private datasets not necessarily be committed to Git?

answer:
   We don't commit these files because they can be generated again may be too large or may contain private data like passwords, API keys, or raw datasets.

------------------------------------------------------------------

Dockerfile vs Image vs Container

-Dockerfile: A file with instructions to build the Docker image.
-Image: A ready package that contains the app and everything it needs.
-Container: A running instance of the image.

------------------------------------------------------------------

Why use Docker volume/mount?

A Docker volume/mount lets the container read and save data from your computer.
It is useful in data engineering because the data stays safe even if the container stops or is deleted.

------------------------------------------------------------------

Git: A tool that tracks changes in your code and lets you manage different versions of a project.

Docker: A tool that packages your app with everything it needs so it can run the same way on different computers.

------------------------------------------------------------------