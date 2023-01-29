import { React, useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState("");
  var config = { responseType: "blob" };
  let fileToBeSent = null;
  const uploadFile = (e) => {
    e.preventDefault();
    let file = fileToBeSent[0];
    const formData = new FormData();

    formData.append("file", file);

    axios
      .post("http://127.0.0.1:5000/upload", formData, {
        responseType: "arraybuffer",
      })
      .then((res) => {
        console.log(res);
        const blob = new Blob([res.data], { type: "image/png" });
        const url = window.URL.createObjectURL(blob);
        setImage(url);
      })
      .catch((err) => console.warn(err));
  };
  const handleFileSelected = (e) => {
    const files = Array.from(e.target.files);
    console.log("files:", files);
    fileToBeSent = files;
    console.log("fileToBeSent:", fileToBeSent);
  };

  return (
    <div
      style={{
        backgroundColor: "#000000",
        minHeight: "100vh",
        color: "#ffffff",
        fontsize: "20px",
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
        className="App"
      >
        <div
          style={{
            display: "flex",
            padding: "90px",
          }}
        >
          <input type="file" name="file" onChange={handleFileSelected} />
          <button style={{}} onClick={uploadFile}>
            Upload
          </button>
        </div>

        <img
          style={{
            height: "100%",
            maxHeight: "70vw",
            maxWidth: "70vh",
            margin: "30px 0",
          }}
          src={image}
          alt="uploaded"
          hidden={image === ""}
        />
      </div>
    </div>
  );
}

export default App;
