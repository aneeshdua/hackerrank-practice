# Casting Agency

## Introduction
The application models a company that is responsible for producing movies as well as assigning of actors to various movies.

## API Reference

### Endpoints

* MOVIES
    <details>
    <summary>GET</summary>

    1. GET all movies
    * Request URL - /movies
    * Response
        * Success
            * Code - 200
            * Content -
            ```yaml
                {
                    "success": True,
                    "movies": movies
                }
            ```

    2. GET specific movie by id
    * Request URL - /movies/movie_id
    * Request Parameters - movie_id=[integer]
    * Response
        * Success
            * Code - 200
            * Content -
            ```yaml
                {
                    "success": True,
                    "movies": movie
                }
            ```
        
    </details>

    <details>
    <summary>POST</summary>

    * Request URL - /movies/new
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True
             }
            ```   
    </details>

    <details>
    <summary>PATCH</summary>

    * Request URL - /movies/movie_id
    * Request Parameters - movie_id
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "movie": movie
             }
            ```   
    </details>

    <details>
    <summary>DELETE</summary>

    * Request URL - /movies/movie_id
    * Request Parameters - movie_id
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "movie": movie
             }
            ```   
    </details>

* ACTORS
    <details>
    <summary>GET</summary>

    1. GET all actors
    * Request URL - /actors
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "actors": actors
             }
            ```

    2. GET specific actor by id
    * Request URL - /actors/actor_id
    * Request Parameters - actor_id
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "actors": actor
             }
            ```           
    </details>

    <details>
    <summary>POST</summary>

    * Request URL - /actors/new
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True
             }
            ```   
    </details>

    <details>
    <summary>PATCH</summary>

    * Request URL - /actors/actor_id
    * Request Parameters - actor_id
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "actor": actor
             }
            ```   
    </details>

    <details>
    <summary>DELETE</summary>

    * Request URL - /actors/actor_id
    * Request Parameters - actor_id
    * Response
        * Success
            * Code - 200
            * Content - 
            ```yaml
             {
                 "success": True,
                 "actor": actor
             }
            ```   
    </details>
    



### Errors
<!-- Error types chahiye?? -->
<details>
<summary>Unprocessable Entity</summary>

* Response code - 422
* Message - "unprocessable"
</details>

<details>
<summary>Not Found</summary>

* Response code - 404
* Message - "Not Found"
</details>

<details>
<summary>Bad Request</summary>

* Response code - 400
* Message - "Your request was not a correct json"
</details>

<details>
<summary>Authorization Error</summary>

* Response code - ????
* Message - "Authorization Error"
</details>

## Author

Aseem Dua

