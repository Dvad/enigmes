Used with Heroku


# Run locally
Install dependencies:

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

Run:
```python
FLASK_ENV=development flask run

```
go to http://localhost:5000 with your browser to test the website

# Run on heroku
1. create a free heroku account
2. I don't quite remember but something like

```bash
heroku create enigmes
heroku open
heroku domains:add enigmes.osurac.net # You should possess the osurac.net domain and configure its dns
git push heroku

```


# Bookmark
π http://enigme.osurac.net/π«π©ββ€οΈβπ¨β‘οΈπ°ππ€΅/π¨βπβ‘οΈπ«π·βοΈπΊπΈ/ππ°β‘οΈπ©βπ³/ποΈππ¦ππ―β‘οΈπ©ββοΈ/
π http://enigme.osurac.net/π«π©ββ€οΈβπ¨β‘οΈπ°ββοΈππ€΅ββοΈ/π¨βπβ‘οΈπ«π·βοΈπΊπΈ/ππ°β‘οΈπ©βπ³/ποΈππ¦ππ―β‘οΈπ©ββοΈ/π₯πΆ.mp4

π localhost:5000/π«π©ββ€οΈβπ¨β‘οΈπ°ππ€΅/π¨βπβ‘οΈπ«π·βοΈπΊπΈ/ππ°β‘οΈπ©βπ³/ποΈππ¦ππ―β‘οΈπ©ββοΈ/
π localhost:5000/π«π©ββ€οΈβπ¨β‘οΈπ°ββοΈππ€΅ββοΈ/π¨βπβ‘οΈπ«π·βοΈπΊπΈ/ππ°β‘οΈπ©βπ³/ποΈππ¦ππ―β‘οΈπ©ββοΈ/π₯πΆ.mp4
