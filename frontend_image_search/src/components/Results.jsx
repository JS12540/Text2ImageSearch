import { IoIosThumbsUp, IoIosThumbsDown } from 'react-icons/io';

const API_URL = "http://127.0.0.1:8000";

function Row({ documents }) {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'row',
      justifyContent: 'center',
      width: "50vw",
    }}>
      {documents.map((document, index) => (
        <div key={index} style={{
          position: 'relative',
          borderStyle: 'solid',
          borderRadius: '10px',
          width: "20vw",
          height: "20vh",
          margin: "20px",
        }}>
          <div style={{position: 'absolute', top: 0, right: 0}}>
            <button style={{borderRadius: 500}}><IoIosThumbsUp color={'green'}/></button>
            <button style={{borderRadius: 500}}><IoIosThumbsDown color={'red'}/></button>
          </div>
          <img src={API_URL + '/' + document.payload.uri} alt={document.payload.uri} style={{width: '100%', height: '100%'}}/>
        </div>
      ))}
      <br />
    </div>
  );
}

function Results({ list }) {
  return (
    <div>
      {list.map((_, index) => {
        if (index % 3 === 0) {
          return (
            <Row key={index} documents={list.slice(index, index + 3)} />
          );
        } else {
          return null;
        }
      })}
    </div>
  );
}

export { Results };
