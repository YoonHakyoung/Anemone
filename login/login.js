// login.js
const express = require('express');
const mariadb = require('mariadb');
const router = express.Router();

// MariaDB 연결 설정
const pool = mariadb.createPool({
    host: '127.0.0.1',
    user: 'nodejs_admin',
    password: 'admin',
    database: 'nodejs_logindb',
    connectionLimit: 5
});

// 로그인 경로
router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    try {
        const conn = await pool.getConnection();
        const rows = await conn.query('SELECT * FROM users WHERE email = ?', [email]);

        if (rows.length === 0) {
            res.status(401).json({ message: '사용자를 찾을 수 없습니다.' });
        } else {
            const user = rows[0];
            if (password === user.password) {
                res.json({ message: "로그인 성공!", user: { username: user.username, email: user.email } });
            } else {
                res.status(401).json({ message: '비밀번호가 일치하지 않습니다.' });
            }
        }
        conn.release();
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: '서버 에러 발생' });
    }
});

module.exports = router;
