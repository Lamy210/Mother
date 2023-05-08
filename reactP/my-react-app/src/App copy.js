import React,{ useState} from 'react';
import {useDropzone} from 'react-dropzone'
//import { Jumbotron, Container } from 'react-bootstrap';
//import { Jumbotron,Container } from 'react-bootstrap';
//import { Jumbotron, Container } from 'react-bootstrap';
//import {Jumbotron} from 'react-bootstrap';
import {Container} from 'react-bootstrap';



function MyDropzone() {
  const {acceptedFiles,} = useDropzone();
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ))

    const onDrop = async (acceptedFiles) => {
      console.log("onDropOK")
      



      setUploading(true);



      const formData = new FormData();
      formData.append('file', acceptedFiles[0]);
      const response = await fetch('http://127.0.0.1:5000', {//送る先のURL別の場所一応テストでローカルの方に送ってる
        method: 'POST',
        body: formData,
        onUploadProgress: (progressEvent) => {
          const progress = Math.round((progressEvent.loaded / progressEvent.total) * 100);
          setUploadProgress(progress);
        }
      });
      if (response.ok) {
        alert('ファイルがアップロードされました');
      } else {
        alert('ファイルのアップロードに失敗しました');
      }
      setUploading(false);
    }
    const {getRootProps, getInputProps} = useDropzone({accept:'application/pdf',onDrop,});
  
  return (
    <div>
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {uploading ? (
          <progress value={uploadProgress} max="100" />
        ) : (
      <p>ファイルをドロップするか、ここをクリックしてファイルを選択してください</p>
      //<ul>{files}</ul>
        )}
    </div>
    </div>
  );
}
function App() {

  //CheckBox
  const [isChecked1, setIsChecked1] = useState(false);
  const [isChecked2, setIsChecked2] = useState(false);
  const [isChecked3, setIsChecked3] = useState(false);

  const handleCheckbox1Change = (event) => {
    setIsChecked1(event.target.checked);
    setIsChecked2(event.target.checked);
    setIsChecked3(event.target.checked);
  };
  const handleCheckbox2Change = (event) => {
    setIsChecked2(event.target.checked);
  };
  const handleCheckbox3Change = (event) => {
    setIsChecked3(event.target.checked);
  };
  
  return (
    
    <div>

      <Container className="bg-light p-5"><MyDropzone /></Container>

      <input
          type="checkbox"
          checked={isChecked1}
          onChange={handleCheckbox1Change}
          
        />
        All
        <input
          type="checkbox"
          checked={isChecked2}
          onChange={handleCheckbox2Change}
        />
        前期
        <input
          type="checkbox"
          checked={isChecked3}
          onChange={handleCheckbox3Change}
        />


        
    </div>
  );
}

export default App;
