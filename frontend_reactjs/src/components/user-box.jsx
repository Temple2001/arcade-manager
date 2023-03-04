import styled from 'styled-components';
import { YoutubeOutlined } from '@ant-design/icons';
import { Divider, Card } from 'antd';
import chunithm from '../assets/images/chunithm.png'
import maimai from '../assets/images/maimai.png'
import manual from '../assets/images/manual.png'
import sdvx from '../assets/images/sdvx.png'
const { Meta } = Card;

const Container = styled.div`
    margin-bottom: 100px;
`

const Line = styled.div`
    display: flex;
    overflow: auto;
`

const LogCard = styled(Card)`
    margin: 1em;
    min-width: 20em;
    background-color: white;
    p {
        font-size: 12px;
        color: #3b3b3b;
    }
`

const CoverDiv = styled.div`
    height: 7em;
    position: relative;
`

const Cover = styled.img`
    height: 100%;
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
`

const coverImg = {
    '수동 기록됨': manual,
    '사볼 (발키리기체)': sdvx,
    '사볼 (일반기체)': sdvx,
    '츄니즘': chunithm,
    '마이마이': maimai,
}

function toSeconds(str) {
    const strList = str.split(':');
    return parseInt(strList[0]) * 3600 + parseInt(strList[1]) * 60 + parseInt(strList[2]);
}

export default function UserBox({ userId, userLogs }) {
    return (
        <Container id={userId}>
            <Divider style={{ marginBottom: '50px', fontSize: '25px', color: '#E96479', borderColor: '#4D455D' }}>
                {userId}
            </Divider>
            <Line>
                {userLogs.reverse().map((log, index) => (
                    <LogCard
                        key={index}
                        cover={
                            <CoverDiv>
                                <Cover
                                    alt='arcade type'
                                    src={coverImg[log.arcade_type]}
                                />
                            </CoverDiv>
                        }
                        actions={[
                            <a href={'https://youtu.be/' + log.v_id + '?t=' + toSeconds(log.check_time)} target='_blank' rel='noopener noreferrer'>
                                <YoutubeOutlined style={{fontSize: '2em'}} />
                            </a>,
                        ]}
                    >
                        <Meta
                            title={log.arcade_type}
                            description={
                                <div>
                                    <p>{log.log_time}</p>
                                    <p>{log.check_time}</p>
                                    <p>{log.user_name}</p>
                                </div>
                            }>
                        </Meta>
                    </LogCard>
                ))}
            </Line>
        </Container>
    )
}