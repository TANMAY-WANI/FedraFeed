import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useState } from 'react';
import Offcanvas from 'react-bootstrap/Offcanvas';

function Nbar() {
  const [showSidebar,setSidebar] = useState(false)
  const handleClose = () => {
    setSidebar(false);
  }


  const Sidebar = () => {
    return(
      <>
      <Offcanvas show={showSidebar} scroll backdrop onHide={handleClose}>
          <Offcanvas.Header closeButton>
            <Offcanvas.Title className='sidebar-heading'>FedraFeed</Offcanvas.Title>
          </Offcanvas.Header>

          <Offcanvas.Body>
            <div className='sidebar-divs'>
              <p>
                <img src="home.jpg" alt="" height={20} width={20} /> Home
              </p>
            </div>
            <div className='sidebar-divs'>
              <p>

                <img src="explore.png" alt="" height={20} width={20} /> Explore
              </p>
            </div>
            <div className='sidebar-divs'>
              <p>

                <img src="saved.webp" alt="" height={25} width={20} /> Saved
              </p>
            </div>
            <div className='sidebar-divs'>
              <p>

                <img src="subs.png" alt="" height={20} width={20} /> Subscription
              </p>
            </div>
            <div className='sidebar-divs'>
              <p>
                <img src="setting.jpeg" alt="" height={25} width={25} /> Settings
              </p>
            </div>
            <div className='sidebar-divs'>
              <p>
                <img src="logout.png" alt="" height={20} width={20} /> Log Out
              </p>
            </div>
          </Offcanvas.Body>
          <footer>Copyright: FedraFeed 2023</footer>
        </Offcanvas>
      </>
    )
  }

  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="-100 00 200 100" onClick={()=>{setSidebar(true)}}>
          <rect width="100" height="10" rx="5" ry="5" fill="#fff" />
          <rect y="35" width="100" height="10" rx="5" ry="5" fill="#fff" />
          <rect y="70" width="100" height="10" rx="5" ry="5" fill="#fff" />
        </svg>
        <Container>
          <Navbar.Collapse className='justify-content-center'>
            <Nav>
              <Navbar.Brand href="#home"><img src="logo.png" alt="" height={30} width={150} /></Navbar.Brand>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Sidebar/>
    </>
  );
}

export default Nbar;