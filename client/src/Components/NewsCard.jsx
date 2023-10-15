import "./NewsCard.css"
function NewsCard(props) {
  return (<>
    <div className="Ncard">
        <img  src={props.imageLink} alt="News" />
        <div className="card-content">
            <h3>{props.headline}</h3>
            <p>{props.newsBody}</p>
            <a onClick={props.onReadMore} href={props.newsLink} target="_blank" rel="noopener noreferrer" >Read More</a>
            <button onClick={props.onLike} style={{position:'absolute',right:'20px',bottom:'20px',backgroundColor:'inherit',border:'none'}} className="like-btn">
                {/* heart svg */}
                <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" className="bi bi-heart-fill" viewBox="0 0 16 16" style={{color:props.liked?'red':'lightgrey'}}>
                    <path  fillRule="evenodd" d="M8 3.879C9.5 2.29 11.992 2.29 13.5 3.879c1.5 1.59 1.5 4.164 0 5.754L8 15 2.5 9.633C1 8.043 1 5.47 2.5 3.88 3.992 2.29 6.5 2.29 8 3.879z"/>
                </svg>
            </button>

        </div>
    </div>
  </>
  )
}

export default NewsCard