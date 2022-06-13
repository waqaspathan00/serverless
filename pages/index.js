import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
    async function makeRequestApi() {
        const response = await fetch("api/")
        const data = await response.json()
        // console.log(data[0].food)
        console.log(data)
    }

    async function makeRequestDate() {
        const response = await fetch("api/date")
        const data = await response.text()
        console.log(data)
    }



    return (
        <div>
            <button onClick={makeRequestApi}>Make request to api/</button>
            <button onClick={makeRequestDate}>Make request to api/date</button>
        </div>
    )
}
