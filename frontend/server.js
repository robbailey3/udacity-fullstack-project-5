const express = require('express');
const proxy = require('http-proxy-middleware');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 80;

app.use(express.static(path.join(__dirname, 'dist/frontend')));

// https://facebook.github.io/create-react-app/docs/deployment#serving-apps-with-client-side-routing
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, 'dist/frontend/', 'index.html'));
});

app.listen(PORT, () => console.log(`Listening on :${PORT}`));
