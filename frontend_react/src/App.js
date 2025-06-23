import React, { useState } from 'react';
import './App.css';

const FILTERS = [
  { key: 'keinFilter', label: 'Kein Filter' },
  { key: 'defaultFilter', label: 'Standard-Filter' },
];

function App() {
  const [liste, setListe] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('keinFilter');

  const fetchListe = () => {
    setLoading(true);
    setError(null);
    fetch(`/generate_kuer?preset=${filter}`)
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
      <div style={{ marginBottom: '1em' }}>
        {FILTERS.map(f => (
          <button
            key={f.key}
            onClick={() => setFilter(f.key)}
            style={{
              marginRight: '0.5em',
              fontWeight: filter === f.key ? 'bold' : 'normal',
              background: filter === f.key ? '#1976d2' : '#eee',
              color: filter === f.key ? '#fff' : '#222',
              border: '1px solid #1976d2',
              borderRadius: '4px',
              padding: '0.4em 1em',
              cursor: 'pointer',
            }}
          >
            {f.label}
          </button>
        ))}
      </div>
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
