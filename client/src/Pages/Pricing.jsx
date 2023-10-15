import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import Nbar from '../Components/Nbar';

const Pricing = () => {
  const cardStyle = {
    border: 'none', // Add this style to remove the border
  };
  return (
    <>
    <Nbar />
    <Container>
      <h1 className="text-center mt-5">Our Pricing</h1>
      <Row className="mt-4">
        <Col sm={12} md={4}>
          <Card>
            <Card.Header>
              <h3>Basic</h3>
            </Card.Header>
            <Card.Body>
              <h2>₹0/month</h2>
              <ul>
                <li>Personalized News</li>
                <li>Feature 2</li>
                <li>Feature 3</li>
              </ul>
            </Card.Body>
            <Card.Footer>
              <Button variant="primary">Select Plan</Button>
            </Card.Footer>
          </Card>
        </Col>

        <Col sm={12} md={4}>
          <Card>
            <Card.Header>
              <h3>Pro</h3>
            </Card.Header>
            <Card.Body>
            <h2>₹99/month</h2>
              <ul>
                <li>Personalized News</li>
                <li>News Archive</li>
                <li>Weakly News Summary</li>
              </ul>
            </Card.Body>
            <Card.Footer>
              <Button variant="primary">Select Plan</Button>
            </Card.Footer>
          </Card>
        </Col>

        <Col sm={12} md={4}>
          <Card>
            <Card.Header>
              <h3>Premium</h3>
            </Card.Header>
            <Card.Body>
              <h2>₹149/month</h2>
              <ul>
                <li>Personalized News</li>
                <li>Weakly News Summary</li>
                <li>Exclusive ChatRoom Access</li>
              </ul>
            </Card.Body>
            <Card.Footer>
              <Button variant="primary">Select Plan</Button>
            </Card.Footer>
          </Card>
        </Col>
      </Row>
      <h2 className="text-center mt-5">Plan Comparisons</h2>
      <Row className="mt-4">
        <Col sm={12}>
          <Card style={cardStyle}>
            <Card.Body>
              <table className="table">
                <thead>
                  <tr>
                    <th>Features</th>
                    <th>Basic</th>
                    <th>Pro</th>
                    <th>Premium</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Personalized News Recommendations</td>
                    <td>✓</td>
                    <td>✓</td>
                    <td>✓</td>
                  </tr>
                  <tr>
                    <td>Weekly News Summary</td>
                    <td></td>
                    <td>✓</td>
                    <td>✓</td>
                  </tr>
                  <tr>
                    <td>News Archive</td>
                    <td></td>
                    <td>✓</td>
                    <td>✓</td>
                  </tr>
                  <tr>
                    <td>ChatRoom</td>
                    <td></td>
                    <td></td>
                    <td>✓</td>
                  </tr>
                  
                </tbody>
              </table>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
    </>
  );
};

export default Pricing;
