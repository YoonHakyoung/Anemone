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

// 회원가입 경로
router.post('/register', async (req, res) => {
    const { username, email, password } = req.body;
    try {
        const conn = await pool.getConnection();
        const result = await conn.query("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", [username, email, password]);
        conn.release();

        if (result.affectedRows === 1) {
            res.redirect('login.html'); // 회원가입 성공 시 login.html로 리디렉션
        } else {
            res.json({ message: "회원가입 실패." });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "서버 에러 발생" });
    }
});

module.exports = router;
