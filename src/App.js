import { useState, useEffect } from 'react';
import React, { Component } from 'react';
import FloatingLabelInput from 'react-floating-label-input';
import './App.css';
import wikiMapLogo from './WikiMap.png';

function App() {

  const [source, setSource] = useState("");
  const [dest, setDest] = useState("");


  const handleChangeSrc = (e) => {
    setSource(e.target.value);
  }
  const handleChangeDest = (e) => {
    setDest(e.target.value);
  }

  const handleSubmit = (e) => {
    //pass source and dest into api
      e.preventDefault();
      //call api function
      fetch('/movies.json')
        .then(res => res.json())
        .then(data => {
          console.log(data)
        });
      // console.log(source);
      // console.log(dest);
  }

  return (
    <div className="App">
      <header className="Header">
        <a href="#"><img src={wikiMapLogo} className="logoSize"/></a>
        <p>Finding links for you in the Wiki world.</p>
      </header>
      <div className="container">
        <div className="input-field">
            <FloatingLabelInput className="input" label="Source" id="source" onChange={handleChangeSrc} />
        </div>
        <div className="input-field">
            <FloatingLabelInput className="input" label="Destination" id="destination" onChange={handleChangeDest} />
            <button className="Button-style" onClick={handleSubmit}>Find</button>
        </div>
      </div>           
    </div>
  );
}

export default App;