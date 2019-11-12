import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import TopNav from './TopNav';
import SideNav from './SideNav';
import Chart from './Chart';
import './App.css';

function App() {
  return (
    <div className="App">
      <TopNav></TopNav>
      <Container className="body" fluid>
        <Row style={{ minHeight: "95vh" }}>
          <SideNav />
          <Chart />
        </Row>
      </Container>
    </div>
  );
}

export default App;
