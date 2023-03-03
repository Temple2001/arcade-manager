import styled from 'styled-components';
import UserBox from './user-box';

const Container = styled.div`
    text-align: center;
    background: 
        linear-gradient(
            to top,
            rgba(255, 255, 255, 0) 85%,
            rgba(255, 255, 255, 0.5) 90%,
            rgba(255, 255, 255, 0.7) 95%,
            rgba(255, 255, 255, 0.9) 98%,
            rgba(255, 255, 255, 1) 100%
        ),
        linear-gradient(
            to left,
            rgba(255, 255, 255, 0) 97%,
            rgba(255, 255, 255, 1) 100%
        ),
        linear-gradient(
            to right,
            rgba(255, 255, 255, 0) 98%,
            rgba(255, 255, 255, 1) 100%
        );
    background-color: #F0F2F5;
    padding: 100px 10% 300px 10%;
    @media screen and (max-width: 800px) {
        padding: 100px 0 300px 0;
    }
    z-index: -1;
`

export default function MainContent({ logs, users }) {
    return (
        <Container>
            {users.map((user, index) => (
                <UserBox key={index} userId={user} userLogs={logs.filter(log => log.user_name === user)} />
            ))}
        </Container>
    );
}
