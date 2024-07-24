import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const BarFinder = () => {
  const [district, setDistrict] = useState("")
  const [bars, setBars] = useState([])
  const [randomBar, setRandomBar] = useState(null)
  
  const handleSearch = () => {
    
    axios.get(`http://127.0.0.1:8000/api/places/?district=${district}`)
    .then(response => setBars(response.data))
    setRandomBar(null)
  }

  const handleRandomSelect = () => {
    if(bars.length > 0){
      const randomIndex = Math.floor(Math.random() * bars.length)
      setRandomBar(bars[randomIndex])
    }
  }

  const handleClear = () => {
    setDistrict("");
    setBars([]);
    setRandomBar(null);
  };

  return (
    <div>
      <h1>Find Bars</h1>
      <input
        type="text"
        value={district}
        onChange={e => setDistrict(e.target.value)}
        placeholder="Enter district"
      />
      <button onClick={handleSearch}>Search</button>
      <button onClick={handleRandomSelect} disabled={bars.length === 0}>Randomly Selected Bar</button>
      <button onClick={handleClear}>Clear</button>

      <ul>
        {bars.map(bar => (
          <li key={bar.place_id}>{bar.name} - {bar.vicinity}</li>
        ))}
      </ul>

      {randomBar && (
        <div>
          <h2>The Chosen One Bar</h2>
          <p>{randomBar.name} - {randomBar.vicinity}</p>
        </div>
      )}
    </div>
  )
}



function App() {
  return (
    <div className="App">
      <main>
        <BarFinder />
      </main>
    </div>
  );
}

export default App;
