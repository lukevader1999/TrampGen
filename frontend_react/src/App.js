import React, { useState } from 'react';
import './App.css';

function App() {
  const [liste, setListe] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchListe = () => {
    setLoading(true);
    setError(null);
    fetch('/generate_kuer')
      .then(res => {
        if (!res.ok) throw new Error('Fehler beim Laden der Liste');
        return res.json();
      })
      .then(data => {
        setListe(data.liste)
      })
      .catch(err => {
        setError(err.message)
      })
      .finally(() => {
        setLoading(false)
      });
  };

  return (
    <div className="App">
      <h1>Kür-Generator</h1>
      <button onClick={fetchListe} disabled={loading}>
        {loading ? 'Lade...' : 'Neue Kür generieren'}
      </button>
      {error && <p style={{color: 'red'}}>{error}</p>}
      <ol className="kuer-liste">
        {liste.map((item, idx) => (
          <li key={idx} className="kuer-item">
            <span className="kuer-nummer">{idx + 1}.</span> {item}
          </li>
        ))}
      </ol>
    </div>
  );
}

export default App;
