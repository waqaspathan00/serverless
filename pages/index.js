import React, {useState} from "react";

// submit a food and you should see "successfully submitted x"

export default function Home() {
    const [food, setFood] = useState();

    async function makeRequestApi() {

        const response = await fetch('https://us-central1-learnfirebase-544b9.cloudfunctions.net/get_food?food=pizza')
        const data = await response.json()
        setFood(data.food)
    }

    return (
        <div>
            <button onClick={makeRequestApi}>Make request to api/</button>
            {food && <div>Successfully submitted for {food}</div>}
        </div>
    )
}
