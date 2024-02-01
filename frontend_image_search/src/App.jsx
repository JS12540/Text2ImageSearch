import { useState } from 'react'
import logo from './researcher.png';
import './App.css'
import { Results } from './components/Results'
import Header from './components/Header';

const API_URL = "http://127.0.0.1:8000";

/**
 * A React component for the App.
 *
 * @return {JSX.Element} The JSX for the App component
 */
function App() {
  const [list, setList] = useState([]);
  const [textInput, setTextInput] = useState("");

  /**
   * A function to handle key down events.
   *
   * @param {Event} e - the key down event
   * @return {void} 
   */
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      search(textInput);
    }
  }

  /**
   * A function to perform a search using the provided query.
   *
   * @param {string} query - The search query to be used
   * @return {void} No return value
   */
  const search = (query) => {
    try {
      fetch(API_URL + '?query=' + query)
        .then((response) => response.json())
        .then((response) => {
          setList(response.result); // Update to set the list correctly
          setTextInput(""); // Reset input after search
        })
        .catch((error) => {
          console.log('ERROR!', error);
        });
    } catch (error) {
      console.log('ERROR!', error);
    }
  }

  const onSubmit = () => {
    search(textInput);
  }

  const onChange = (e) => {
    setTextInput(e.target.value)
  }

  return (
    <div>
      <Header />
      <div style={{
        display: "flex",
        justifyContent: "center"
      }}>
        <a target="_blank">
          <img src={logo} className="logo" alt="Vite logo" />
        </a>
        <h1>Multi-Modal Search</h1>
      </div>

      <div style={{
        display: "flex",
        justifyContent: "center",
        width: "1280px"
      }}>
        <div>
          <p>
            Search for and retrieve objects visible from satellite imagery.
          </p>
          <p className="read-the-docs">
            This tool helps you to find examples. It is not an exhaustive search.
          </p>
          <div>
            <input
              style={{ marginTop: 10, marginBottom: 20, height: 30, width: "30vw" }}
              type="text"
              value={textInput}
              onChange={onChange}
            />
            <button style={{ width: "10vw", margin: 5 }} onClick={onSubmit} onKeyDown={handleKeyDown}>
              Search
            </button>
          </div>
          <div style={{ borderStyle: 'solid', width: "50vw", height: "50vh", overflowY: "scroll" }}>
            <Results list={list} />
          </div>
        </div>
      </div>
    </div>
  )
}

export default App;
