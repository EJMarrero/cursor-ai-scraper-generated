const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
app.options('*', cors());

app.get('/api/opiniones', (req, res) => {
  res.json({ message: 'Opiniones' });
});

app.listen(5000, () => console.log('Servidor iniciado en el puerto 5000')); 