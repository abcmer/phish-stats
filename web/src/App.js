import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import NavBar from './NavBar';
import SideNav from './SideNav';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <div style={{ minHeight: "100vh" }}>
        <Container style={{ minHeight: "100vh" }} fluid>
          <Row style={{ minHeight: "100vh" }}>
            <Col xs lg="2" className="side-bar">Side Bar</Col>
            <Col className="main-content">Main Content</Col>
          </Row>
        </Container>
      </div>
    </div>
  );
}

export default App;
