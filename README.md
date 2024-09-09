# Contacts App (Flask)

My copy of the [official Flask example][htmx-proj] application with an extra dash of last decade's style
and stripped of any [htmx][htmx] directives for a clean start. I created this version to follow
along with the book [Hypermedia Systems][htmx-book] starting at [Chapter 05](https://hypermedia.systems/htmx-patterns/).

## Note

- This project uses the [Library Manager][libman] [CLI][libman-cli] to manage client-side libraries. You do not need it, 
    but I find if you have .NET on your system it is really handy for handling non-bundled client-side assets.

  ```shell
  # Install the client-side libraries
  libman restore
  ```
- I will win no awards for design in my lifetime and I am okay with this.


[htmx]: https://htmx.org "High power tools for HTML"
[htmx-book]: https://hypermedia.systems/ "Hypermedia Systems Book"
[flask]: https://flask.palletsprojects.com/ "Flask - A minimal web framework for Python"
[htmx-proj]: https://github.com/bigskysoftware/contact-app "Contact App - official"
[libman]: https://devblogs.microsoft.com/dotnet/library-manager-client-side-content-manager-for-web-apps/ "Client-side content manager for web apps"

[libman-cli]: https://learn.microsoft.com/en-us/aspnet/core/client-side/libman/libman-cli