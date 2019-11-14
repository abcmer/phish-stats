import React, { useState, useEffect, useRef } from 'react';
import { Col } from 'react-bootstrap';

const generateDataset = () => (
  Array(10).fill(0).map(() => ([
    Math.random() * 80 + 10,
    Math.random() * 35 + 10,
  ]))
)

function useInterval(callback, delay) {
  const savedCallback = useRef();

  // Remember the latest callback.
  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  // Set up the interval.
  useEffect(() => {
    function tick() {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
}

const Rectangles = () => {
  const [dataset, setDataset] = useState(
    generateDataset()
  )
  useInterval(() => {
    const newDataset = generateDataset()
    setDataset(newDataset)
  }, 2000)
  return (
    <Col>
      <svg viewBox="0 0 100 50">
        {dataset.map(([x, y], i) => (
          <rect
            width={x}
            height={y}
            style={{ fill: "rgb(0,0,255)", strokeWidth: "3", stroke: "rgb(0,0,0)" }}
          />
        ))}
      </svg>
    </Col>
  )
}

export default Rectangles