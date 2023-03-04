import { useState, useEffect } from 'react';
import styled from 'styled-components';
import MainContent from './main-content';
import MainMenu from './main-menu';
import ApiClient from '../scripts/api-client';
const client = new ApiClient();

const TopBackground = styled.div`
    background: linear-gradient(
        to bottom,
        rgba(255, 255, 255, 0) 85%,
        rgba(255, 255, 255, 0.5) 90%,
        rgba(255, 255, 255, 0.7) 95%,
        rgba(255, 255, 255, 1) 100%
    ),
    URL(https://eacache.s.konaminet.jp/game/sdvx/vi/images/top/main_sp.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 50% 35%;
    opacity: 0.6;
    filter: blur(2px);
    width: 100%;
    height: 300px;
`

const TopTitle = styled.h1`
    font-family: 'nanumgothic';
    text-align: center;
    font-size: 40px;
    position: absolute;
    top: 130px;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    width: max-content;
    background-color: rgba(0, 0, 0, 0.7);
    border-radius: 10px;
    margin: 0;
`

export function Main() {
    const [logs, setLogs] = useState([]);
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const getDataProcess = async () => {
            const res = await client.getData();
            setLogs(res);

            const dupRemove = res.filter((item1, idx1) => {
                return res.findIndex((item2, idx2) => {
                    return item1.user_name === item2.user_name;
                }) === idx1;
            });
            const users = dupRemove.map((value) => (value.user_name));
            setUsers(users);
        }
        getDataProcess();
    }, []);

    return (
        <div id='top'>
            <TopBackground />
            <TopTitle>
                &nbsp;Arcade Manager&nbsp;
            </TopTitle>

            <MainMenu users={users} />
            <MainContent logs={logs} users={users} />
        </div>
    );
}

export default Main;