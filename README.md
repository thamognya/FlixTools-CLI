# FlixTools

This repo used to contain shell scripts and still does in the [ShellScript branch](https://github.com/thamognya/FlixTools/tree/ShellScripts)

# Frameworks

Frontend:

Makes api calls to backend to get video link

- TailwindCSS
- Chakra UI
- Sass
- NextJS

or

- React Native

or 
*
- Flutter

Backend:

Interacts with streaming services for video link

*
- Django
- Django Graphql with graphene or rest framework

### Big Topic
/manga -> for manga
/anime -> for anime
/movie -> for movies
/book -> for books

json format:

```json
{
    "popular": [{"_name_": "_thumnail_link_"}, ...],
}
```

### Small Topic

/manga/name-name
/anime/name-name
/movie/name-name
/book/name-name

```json
{
    "episodes": [{"_epi_name_": "_thumnail_": "_video_"}]
}
