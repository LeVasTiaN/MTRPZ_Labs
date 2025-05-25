const express = require('express');
const mongoose = require('mongoose');
const app = express();
app.use(express.json());

mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/wordstream');

const Word = mongoose.model('Word', new mongoose.Schema({
  word: String,
  createdAt: { type: Date, default: Date.now }
}));

app.post('/word', async (req, res) => {
  try {
    await Word.create({ word: req.body.word });
    res.send("Word saved");
  } catch (e) {
    res.status(500).send("Error");
  }
});

app.get('/', async (req, res) => {
  try {
    const words = await Word.find().sort({ createdAt: -1 }).limit(20);
    res.send(`
      <form method="post" action="/word" onsubmit="fetch('/word',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({word:document.getElementById('w').value})}).then(()=>location.reload());return false;">
        <input id="w" placeholder="Enter a word"/>
        <button>Submit</button>
      </form>
      <h2>Recent words</h2>
      <ul>${words.map(w => `<li>${w.word} (${new Date(w.createdAt).toLocaleString()})</li>`).join('')}</ul>
    `);
  } catch (e) {
    res.status(500).send("Error fetching words");
  }
});

app.listen(3000, () => console.log("Listening on http://localhost:3000"));
