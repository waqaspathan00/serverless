import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
    async function makeRequest() {
        const response = await fetch("api/")
        const data = await response.json()
        // console.log(data[0].food)
        console.log(data)
    }

    return (
        <div>
            <button onClick={makeRequest}>Make request to api/index</button>
            <button onClick={makeRequest}>Make request to api/date</button>
        </div>
    )
}
