
![Bift_](https://user-images.githubusercontent.com/38106396/215903942-65daf2f3-f349-4c60-90da-be692effbf30.png)


# Bift - Blog-site
Bift is a beginner friendly blog project using `Django` and `Flowbite`.

## How To Use
To clone and run this, you will need `git` and [pip](https://pip.pypa.io/en/stable/installation/).
```
# Clone this repository
$ git clone git@github.com:devbilalkhan/Bift---Blog-site.git

# Move into the mysite folder
$ cd mysite

# Create and activate virtual environment
$ pip install virtualenv
$ source env/bin/activate

# Install packages from requirements.txt
$ pip install -r requirements.txt

# Run the app
$ python3 manage.py runserver

# Run following in a separate terminal under the same folder
# This command watches for changes and compiles the tailwind css code
$ npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch

```


Load environment variables from `.env` file. See the same `.env-sample` file.
