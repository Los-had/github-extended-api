# github-extended-api 
more functions for the github api.

### documentation
read the documentation in:
[https://github-extended-api/docs](https://github-extended-api/docs)

## features
* get user pinned repos
* get all user repos
* get user repo by name
* get all user info 
* get user info with filter

## installing on your machine

download the project on github. 

```
$ git clone <repo url>
``` 

After that open your terminal and write:

```
$ cd github-extended-api 
    # enter in the app folder
$ pip install -r requirements.txt
    # install the dependencies
$ uvicorn app:app
    # execute the app
```

This commands wiil execute the script in: 

```
http://127.0.0.1:8000
```

to stop the server(localhost) press <kbd>Ctrl</kbd><kbd>+</kbd><kbd>C</kbd> or <kbd>Cmd</kbd><kbd>+</kbd><kbd>C</kbd>


## License
[MIT](LICENSE)