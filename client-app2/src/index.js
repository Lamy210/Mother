// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Appコンポーネントがあると仮定します
//import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
