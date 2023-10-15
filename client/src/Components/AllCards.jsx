import NewsCard from "./NewsCard";
import "./AllCards.css"
import { useEffect, useState } from "react";
import axios from "axios";
import { Button } from "react-bootstrap";

function AllCards() {
    const [data, setData] = useState([]);
    const [liked, setLiked] = useState([]);
    const [page, setPage] = useState(1);
    useEffect(() => {
        // axios.post('http:localhost:5001/api/')
        setData([
            {headline:'Husband hugs wife to calm her after fight on railway track, both run over by train in UP',
        newsBody:`A 30-year-old man and his wife were run over by a train when he hugged her and was trying to calm her down on railway tracks after a fight in Uttar Pradesh's Varanasi. She had gone to the tracks to take her life due to the man's alcohol addiction and he was trying to stop her. They have three children.`,
        imageLink:`https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/10_oct/13_fri/img_1697216994472_840.jpg?`,
        newsLink:`https://www.timesnownews.com/india/varanasi-news-husband-hugs-wife-to-calm-her-after-fight-both-run-over-by-train-article-104406805/amp?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts
        `
        },
            {headline:'Husband hugs wife to calm her after fight on railway track, both run over by train in UP',
        newsBody:`A 30-year-old man and his wife were run over by a train when he hugged her and was trying to calm her down on railway tracks after a fight in Uttar Pradesh's Varanasi. She had gone to the tracks to take her life due to the man's alcohol addiction and he was trying to stop her. They have three children.`,
        imageLink:`https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/10_oct/13_fri/img_1697216994472_840.jpg?`,
        newsLink:`https://www.timesnownews.com/india/varanasi-news-husband-hugs-wife-to-calm-her-after-fight-both-run-over-by-train-article-104406805/amp?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts
        `
        },
        ]);
    }, [page]);
    useEffect(() => {
        setLiked(Array(data.length).fill(false));
    }, [data]);

    function handleLike(index){
        setLiked((prevLiked) => {
            let temp = [...prevLiked];
            temp[index] = !temp[index];
            return temp;
        });
    }
    function onReadMore(index){
        if(liked[index]){
            return;
        }
        setLiked((prevLiked)=>{
            let temp = [...prevLiked];
            temp[index] = true;
            return temp;
        })
    }
    function readMore(){
        // axios.post('http:localhost:5001/api/') //send like data and fetch new data

        setPage(page+1);
    }
    return (<>
        <div className="cards">
            {data.map((each, index) => {
                return <NewsCard key={index} liked={liked[index]} onReadMore={()=>onReadMore(index)} onLike={()=>handleLike(index)}  {...each} />;
            })}
        </div>
        <Button className="btn btn-success" style={{display:'flex',margin:'0 auto'}} onClick={()=>readMore()}>Read More</Button>
        </>);
}

export default AllCards;
