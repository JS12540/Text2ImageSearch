import React from "react";

function ImageDisplay({ images }) {
  return (
    <div className="ImageDisplay">
      {images.map((image, index) => (
        <img key={index} src={image} alt={`Image ${index}`} />
      ))}
    </div>
  );
}

export default ImageDisplay;
