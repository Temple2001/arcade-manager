import styled from 'styled-components';
import { useEffect, useState, useRef } from 'react';
import { Menu, ConfigProvider } from 'antd';
import { Link } from 'react-scroll';

const scrollOffset = -50;

const MenuWrapper = styled.div`
    .non-fixed-top {
        position: absolute;
        top: 295px;
        left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 10px;
        padding: 0px 5px 0px 5px;
        box-shadow: 0px 1px 2px 1px #cf95a9;
    }
    .fixed-top {
        position: fixed;
        top: 0%;
        left: 50%;
        transform: translate(-50%, 0);
        border-radius: 10px;
        padding: 0px 5px 0px 5px;
        box-shadow: 0px 5px 10px 5px #cf95a9;
        z-index: 1;
    }
`

const MenuBar = styled(Menu)`
    
`

export default function MainMenu({ users }) {
    const [items, setItems] = useState([]);
    const [fixedTop, setFixedTop] = useState(false);
    const menuBarWrapper = useRef(null);

    const onScroll = () => {
        if (
            window.scrollY > 0 &&
            menuBarWrapper.current.getBoundingClientRect().top <= 0
        ) {
            setFixedTop(true);
        } else {
            setFixedTop(false);
        }
    };

    useEffect(() => {
        const items = users.map((user, index) => {
            return {
                label: <Link to={user} spy={false} smooth={true} offset={scrollOffset}>{user}</Link>,
                key: index,
            }
        });
        setItems(items);

        window.addEventListener('scroll', onScroll);
        return () => {
            window.removeEventListener('scroll', onScroll);
        };
    }, [users]);
    
    return (
        <ConfigProvider
            theme={{
                token: {
                    colorPrimary: '#D61355',
                },
            }}
        >
            <MenuWrapper ref={menuBarWrapper}>
                <MenuBar
                    className={fixedTop ? 'fixed-top' : 'non-fixed-top'}
                    theme='light'
                    mode='horizontal'
                    selectable={false}
                    items={items}
                />
            </MenuWrapper>
            
        </ConfigProvider>
    )
}
