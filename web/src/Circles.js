import React, { useState, useEffect, useRef } from 'react';

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

const Circles = () => {
  const [dataset, setDataset] = useState(
    generateDataset()
  )
  useInterval(() => {
    const newDataset = generateDataset()
    setDataset(newDataset)
  }, 2000)
  return (
    <svg viewBox="0 0 100 50">
      {dataset.map(([x, y], i) => (
        <circle
          cx={x}
          cy={y}
          r="3"
        />
      ))}
    </svg>
  )
}

export default Circles