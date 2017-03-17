from github import Github
from flask import Flask
from sys import argv
from github.Repository import Repository as repository_class
from github import UnknownObjectException
from github.GithubException import RateLimitExceededException

app = Flask(__name__)

url_string = argv[1]

url_split_list = url_string.rsplit("/",2)

@app.route("/")
def hello():
    return "This is the default home page. Configuration files content can be seen at url /v1/your_config_filename"


@app.route("/v1/<filename>")
def file_content(filename):
    result = ""
    repo = ""
    try:
        repo = Github().get_user(url_split_list[1]).get_repo(url_split_list[2])
        result =  repo.get_file_contents(filename).decoded_content
    except RateLimitExceededException:
        result = "Github API rate limit exceeded!!. Try Again"
    except UnknownObjectException:
        if type(repo) is not repository_class:
            result = "The run time URL didn't point to a valid github repository. Please provide a valid URL."
        elif "json" in filename:
            result = "This JSON file is not available."
        elif "yml" in filename:
            result = "This YML file is not available."
        else :
            result = "This is not a valid configuration file."  
    finally:
        return result

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')
