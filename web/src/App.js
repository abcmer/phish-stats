import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import TopNav from './TopNav';
import Circles from './viz/Circles';
import Rectangles from './viz/Rectangles';
import Home from './Home';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <TopNav />
        <Container className="body" fluid>
          <Row style={{ minHeight: "95vh" }}>
            <Col lg="2" className="sidebar">
              <Link to="/shows-per-year"><div className="sidebar-item">Shows Per Year</div></Link>
              <Link to="/shows-by-state"><div className="sidebar-item">Shows By State</div></Link>
            </Col>
            <Col>
              <Switch>
                <Route path="/shows-per-year">
                  <Circles />
                </Route>
                <Route path="/shows-by-state">
                  <Rectangles />
                </Route>
                <Route path="/">
                  <Home />
                </Route>
              </Switch>
            </Col>
          </Row>
        </Container>
      </div>
    </Router>
  );
}

export default App;
