# 📚 Документация базы данных

## Содержание
1. [Общая информация](#общая-информация)
2. [Диаграмма ER](#диаграмма-er)
3. [Описание таблиц](#описание-таблиц)
4. [Связи между таблицами](#связи-между-таблицами)
5. [Ограничения и правила целостности](#ограничения-и-правила-целостности)

---

## Общая информация

**Название БД:** `university_db`  
**Тип СУБД:** MySQL 8.0.43  
**Кодировка:** UTF8MB4 (поддержка Unicode)  
**Назначение:** Управление учебным процессом университета  
**Последнее обновление:** 17 декабря 2025

### Основные сущности:
- **Студенты** — 6 студентов, обучающихся в 4 группах
- **Преподаватели** — 4 преподавателя из 3 кафедр
- **Предметы** — 5 дисциплин (3 математических, 2 гуманитарных)
- **Записи (Enrollments)** — 20 записей студентов на предметы
- **Оценки (Grades)** — 25 оценок студентов
- **Назначения преподавателей** — 12 распределений преподавателей на предметы

_(количественные данные на конец выполнения задания: что-то добавлялось, что-то удалялось по ходу исполнения запросов)
_

---

## Диаграмма ER

```
┌──────────────┐
│   STUDENTS   │
├──────────────┤
│ student_id* │
│ full_name   │
│ birth_date  │
│ email       │
│ phone       │
│ group_number│
└──────────────┘
        │
        ├─────────────────┬──────────────────┐
        │                 │                  │
        ▼                 ▼                  ▼
┌──────────────────┐  ┌──────────┐  ┌──────────────┐
│   ENROLLMENTS    │  │  GRADES  │  │   SUBJECTS   │
├──────────────────┤  ├──────────┤  ├──────────────┤
│ enrollment_id*   │  │ grade_id*│  │ subject_id*  │
│ student_id(FK)───┼──┤ student_ │  │ subject_name │
│ subject_id(FK)   │  │ id(FK)───┼──┤ category     │
│ academic_year    │  │ subject_ │  │ description  │
│ semester         │  │ id(FK)   │  │ credits      │
│ enrolled_date    │  │ teacher_ │  └──────────────┘
└──────────────────┘  │ id(FK)───┐        ▲
                      │ grade    │        │
        ┌─────────────▶│ grade_   │        │
        │              │ date     │        │
        │              │ academic_│        │
        │              │ year     │        │
        │              │ semester │        │
        │              └──────────┘        │
        │                                  │
┌───────┴─────────────────────────────────┤
│                                          │
│    ┌──────────────┐                     │
│    │   TEACHERS   │                     │
│    ├──────────────┤                     │
│    │ teacher_id*  │                     │
│    │ full_name    │                     │
│    │ birth_date   │                     │
│    │ email        │                     │
│    │ phone        │                     │
│    │ department   │                     │
│    └──────────────┘                     │
│            │                            │
│            ▼                            │
│    ┌────────────────────────┐           │
│    │ TEACHING_ASSIGNMENTS   │           │
│    ├────────────────────────┤           │
│    │ assignment_id*         │           │
│    │ teacher_id(FK)─────────┼───────────┘
│    │ subject_id(FK)─────────┼───────────┐
│    │ academic_year          │           │
│    │ semester               │           │
│    │ assigned_date          │           │
│    └────────────────────────┘           │
│                                         │
└─────────────────────────────────────────┘

* = PRIMARY KEY
FK = FOREIGN KEY
```

---

## Описание таблиц

### 1️⃣ STUDENTS (Студенты)

**Назначение:** Хранение информации о студентах  
**Количество записей:** 6 студентов

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `student_id` | INT | Уникальный идентификатор студента | PRIMARY KEY, AUTO_INCREMENT |
| `full_name` | VARCHAR(255) | Полное имя студента | NOT NULL, INDEXED |
| `birth_date` | DATE | Дата рождения | NOT NULL |
| `email` | VARCHAR(50) | Электронная почта | OPTIONAL, INDEXED, FORMAT CHECK |
| `phone` | VARCHAR(20) | Номер телефона | NOT NULL |
| `group_number` | VARCHAR(20) | Номер учебной группы | OPTIONAL |

**Студенты в БД:**

| student_id | full_name | birth_date | email | group_number |
|---|---|---|---|---|
| 1 | Иван Петров | 2005-03-15 | ivan.petrov@example.com | Б23-01 |
| 2 | Петр Иванов | 2004-05-20 | petr.ivanov@example.com | Б23-01 |
| 3 | Анна Сидорова | 2005-08-10 | anna.sidorova@example.com | Б23-02 |
| 4 | Сергей Смирнов | 2004-11-25 | sergey.smirnov@example.com | Б23-02 |
| 5 | Мария Волкова | 2005-01-30 | maria.volkova@example.com | Б23-03 |
| 8 | Алексей Козлов | 2005-07-12 | alexey.kozlov@example.com | Б23-04 |

---

### 2️⃣ TEACHERS (Преподаватели)

**Назначение:** Хранение информации о преподавателях  
**Количество записей:** 4 преподавателя

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `teacher_id` | INT | Уникальный идентификатор преподавателя | PRIMARY KEY, AUTO_INCREMENT |
| `full_name` | VARCHAR(255) | Полное имя преподавателя | NOT NULL, INDEXED |
| `birth_date` | DATE | Дата рождения | NOT NULL |
| `email` | VARCHAR(50) | Электронная почта | OPTIONAL, INDEXED, FORMAT CHECK |
| `phone` | VARCHAR(20) | Номер телефона | NOT NULL |
| `department` | VARCHAR(100) | Кафедра/Отделение | NOT NULL |

**Преподаватели в БД:**

| teacher_id | full_name | department | email |
|---|---|---|---|
| 1 | Дмитрий Калугин | Кафедра математики | dmitry.new@example.com |
| 2 | Елена Петрова | Кафедра истории | elena.petrova@example.com |
| 3 | Владимир Сидоров | Кафедра математики | vladimir.sidorov@example.com |
| 4 | Ольга Смирнова | Кафедра иностранных языков | olga.smirnova@example.com |

---

### 3️⃣ SUBJECTS (Предметы)

**Назначение:** Хранение информации об учебных дисциплинах  
**Количество записей:** 5 предметов

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `subject_id` | INT | Уникальный идентификатор предмета | PRIMARY KEY, AUTO_INCREMENT |
| `subject_name` | VARCHAR(255) | Название предмета | NOT NULL |
| `category` | VARCHAR(50) | Категория предмета | NOT NULL, CHECK CONSTRAINT |
| `description` | TEXT | Описание содержания предмета | OPTIONAL |
| `credits` | INT | Количество кредитов | OPTIONAL |

**Возможные категории:**
- Математические
- Гуманитарные
- Естественные
- Прочие

**Предметы в БД:**

| subject_id | subject_name | category | credits | description |
|---|---|---|---|---|
| 1 | Математика | Математические | 4 | Основы математического анализа |
| 2 | Алгебра | Математические | 3 | Линейная алгебра и матрицы |
| 3 | История России | Гуманитарные | 3 | История России XX века |
| 4 | Английский язык | Гуманитарные | 4 | Практический английский язык |
| 6 | Дифференциальные уравнения | Математические | 4 | Теория дифференциальных уравнений |

---

### 4️⃣ ENROLLMENTS (Записи студентов на предметы)

**Назначение:** Регистрация записи студента на изучение предмета в определенном семестре  
**Количество записей:** 20 записей  
**Связь многие-ко-многим:** между STUDENTS и SUBJECTS через ACADEMIC_YEAR и SEMESTER

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `enrollment_id` | INT | Уникальный идентификатор записи | PRIMARY KEY, AUTO_INCREMENT |
| `student_id` | INT | ID студента | NOT NULL, FOREIGN KEY → STUDENTS |
| `subject_id` | INT | ID предмета | NOT NULL, FOREIGN KEY → SUBJECTS |
| `academic_year` | VARCHAR(9) | Учебный год (формат: YYYY-YYYY) | NOT NULL |
| `semester` | INT | Номер семестра | NOT NULL, CHECK (1 или 2) |
| `enrolled_date` | DATE | Дата записи на предмет | OPTIONAL |

**Первичный ключ:** `enrollment_id`

**Уникальное ограничение (UNIQUE KEY):**
- Комбинация (student_id, subject_id, academic_year, semester)
- **Смысл:** Студент не может быть записан дважды на один и тот же предмет в одном семестре одного учебного года

**Примеры записей:**

| enrollment_id | student_id | subject_id | academic_year | semester | enrolled_date |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2024-2025 | 1 | 2025-12-16 |
| 2 | 1 | 3 | 2024-2025 | 1 | 2025-12-16 |
| 3 | 1 | 4 | 2024-2025 | 1 | 2025-12-16 |
| 4 | 2 | 1 | 2024-2025 | 1 | 2025-12-16 |
| 5 | 2 | 2 | 2024-2025 | 2 | 2025-12-16 |

---

### 5️⃣ GRADES (Оценки)

**Назначение:** Хранение оценок студентов за предметы  
**Количество записей:** 25 оценок

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `grade_id` | INT | Уникальный идентификатор оценки | PRIMARY KEY, AUTO_INCREMENT |
| `student_id` | INT | ID студента | NOT NULL, FOREIGN KEY → STUDENTS |
| `subject_id` | INT | ID предмета | NOT NULL, FOREIGN KEY → SUBJECTS |
| `teacher_id` | INT | ID преподавателя, выставившего оценку | NOT NULL, FOREIGN KEY → TEACHERS |
| `grade` | INT | Значение оценки | NOT NULL, CHECK (1-5) |
| `grade_date` | DATE | Дата выставления оценки | OPTIONAL |
| `academic_year` | VARCHAR(9) | Учебный год | NOT NULL |
| `semester` | INT | Номер семестра | NOT NULL, CHECK (1 или 2) |

**Первичный ключ:** `grade_id`

**Проверка целостности:**
- `grade` должна быть от 1 до 5 (включительно)
- `semester` должен быть 1 или 2

**Шкала оценок:**
| Оценка | Интерпретация |
|--------|--------------|
| 5 | Отлично |
| 4 | Хорошо |
| 3 | Удовлетворительно |
| 2 | Неудовлетворительно |
| 1 | Не сдано |

**Примеры оценок:**

| grade_id | student_id | subject_id | teacher_id | grade | academic_year | semester | grade_date |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 5 | 2024-2025 | 1 | 2025-12-16 |
| 2 | 1 | 3 | 2 | 4 | 2024-2025 | 1 | 2025-12-16 |
| 3 | 1 | 4 | 4 | 3 | 2024-2025 | 1 | 2025-12-16 |
| 4 | 2 | 1 | 1 | 4 | 2024-2025 | 1 | 2025-12-16 |
| 5 | 2 | 2 | 1 | 5 | 2024-2025 | 2 | 2025-12-16 |

**Статистика по оценкам:**
- Студент 1: 8 оценок (средняя: 4.25)
- Студент 2: 10 оценок (средняя: 3.3)
- Студент 3: 4 оценки (средняя: 4.25)
- Студент 4: 2 оценки (средняя: 3)
- Студент 5: 1 оценка (средняя: 2.5)

---

### 6️⃣ TEACHING_ASSIGNMENTS (Назначения преподавателей)

**Назначение:** Регистрация распределения преподавателей на преподавание предметов  
**Количество записей:** 12 назначений  
**Связь многие-ко-многим:** между TEACHERS и SUBJECTS через ACADEMIC_YEAR и SEMESTER

| Атрибут | Тип | Описание | Ограничения |
|---------|-----|---------|------------|
| `assignment_id` | INT | Уникальный идентификатор назначения | PRIMARY KEY, AUTO_INCREMENT |
| `teacher_id` | INT | ID преподавателя | NOT NULL, FOREIGN KEY → TEACHERS |
| `subject_id` | INT | ID предмета | NOT NULL, FOREIGN KEY → SUBJECTS |
| `academic_year` | VARCHAR(9) | Учебный год (формат: YYYY-YYYY) | NOT NULL |
| `semester` | INT | Номер семестра | NOT NULL, CHECK (1 или 2) |
| `assigned_date` | DATE | Дата назначения | OPTIONAL |

**Первичный ключ:** `assignment_id`

**Уникальное ограничение (UNIQUE KEY):**
- Комбинация (teacher_id, subject_id, academic_year, semester)
- **Смысл:** Преподаватель не может быть назначен дважды на один и тот же предмет в одном семестре одного учебного года

**Примеры назначений:**

| assignment_id | teacher_id | subject_id | academic_year | semester | assigned_date |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2024-2025 | 1 | 2025-12-16 |
| 2 | 1 | 2 | 2024-2025 | 2 | 2025-12-16 |
| 4 | 3 | 1 | 2024-2025 | 1 | 2025-12-16 |
| 5 | 2 | 3 | 2024-2025 | 1 | 2025-12-16 |
| 6 | 4 | 4 | 2024-2025 | 1 | 2025-12-16 |

**Распределение преподавателей:**
- Преподаватель 1 (Дмитрий Калугин): 5 назначений
- Преподаватель 2 (Елена Петрова): 2 назначения
- Преподаватель 3 (Владимир Сидоров): 1 назначение
- Преподаватель 4 (Ольга Смирнова): 4 назначения

---

## Связи между таблицами

### 📌 STUDENTS ↔ ENROLLMENTS (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:** 
- Один студент может быть записан на **множество предметов**
- Каждая запись принадлежит ровно одному студенту

**Foreign Key:** 
```sql
ENROLLMENTS.student_id → STUDENTS.student_id
ON DELETE CASCADE
```

**Смысл ON DELETE CASCADE:** Если студент удаляется из системы, все его записи на предметы удаляются автоматически

**SQL запрос для проверки:**
```sql
SELECT s.full_name, COUNT(e.enrollment_id) as subject_count
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id;
```

---

### 📌 SUBJECTS ↔ ENROLLMENTS (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один предмет может быть записан на **множество студентов**
- Каждая запись принадлежит ровно одному предмету

**Foreign Key:**
```sql
ENROLLMENTS.subject_id → SUBJECTS.subject_id
ON DELETE CASCADE
```

**Смысл ON DELETE CASCADE:** Если предмет удаляется, все записи студентов на этот предмет удаляются

---

### 📌 STUDENTS ↔ GRADES (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один студент может получить **множество оценок** (по разным предметам)
- Каждая оценка принадлежит ровно одному студенту

**Foreign Key:**
```sql
GRADES.student_id → STUDENTS.student_id
ON DELETE CASCADE
```

---

### 📌 SUBJECTS ↔ GRADES (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один предмет может иметь **множество оценок** (от разных студентов)
- Каждая оценка принадлежит ровно одному предмету

**Foreign Key:**
```sql
GRADES.subject_id → SUBJECTS.subject_id
ON DELETE CASCADE
```

---

### 📌 TEACHERS ↔ GRADES (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один преподаватель может выставить **множество оценок** (разным студентам)
- Каждая оценка выставлена ровно одним преподавателем

**Foreign Key:**
```sql
GRADES.teacher_id → TEACHERS.teacher_id
ON DELETE CASCADE
```

**Статистика:**
- Преподаватель 1: 11 оценок выставлено
- Преподаватель 2: 6 оценок выставлено
- Преподаватель 4: 5 оценок выставлено
- Преподаватель 3: 0 оценок выставлено

---

### 📌 TEACHERS ↔ TEACHING_ASSIGNMENTS (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один преподаватель может быть назначен на **множество предметов**
- Каждое назначение принадлежит ровно одному преподавателю

**Foreign Key:**
```sql
TEACHING_ASSIGNMENTS.teacher_id → TEACHERS.teacher_id
ON DELETE CASCADE
```

---

### 📌 SUBJECTS ↔ TEACHING_ASSIGNMENTS (1 ко многим)

**Тип:** One-to-Many (1:М)

**Описание:**
- Один предмет может быть назначен **множеству преподавателей**
- Каждое назначение связано ровно с одним предметом

**Foreign Key:**
```sql
TEACHING_ASSIGNMENTS.subject_id → SUBJECTS.subject_id
ON DELETE CASCADE
```

---

### 📌 Связь многие-ко-многим: STUDENTS ↔ SUBJECTS (через ENROLLMENTS)

**Тип:** Many-to-Many (М:М)

**Описание:**
- Один студент может изучать **множество предметов**
- Один предмет может изучаться **множеством студентов**

**Таблица связи:** `ENROLLMENTS`

**Визуализация:**
```
STUDENTS ──(1:М)──→ ENROLLMENTS ←──(М:1)── SUBJECTS
```

**SQL запрос для получения всех предметов студента:**
```sql
SELECT s.full_name, subj.subject_name, e.academic_year, e.semester
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN subjects subj ON e.subject_id = subj.subject_id
WHERE s.student_id = ?;
```

---

### 📌 Связь многие-ко-многим: TEACHERS ↔ SUBJECTS (через TEACHING_ASSIGNMENTS)

**Тип:** Many-to-Many (М:М)

**Описание:**
- Один преподаватель может преподавать **множество предметов**
- Один предмет может преподаваться **множеством преподавателей**

**Таблица связи:** `TEACHING_ASSIGNMENTS`

**Визуализация:**
```
TEACHERS ──(1:М)──→ TEACHING_ASSIGNMENTS ←──(М:1)── SUBJECTS
```

**SQL запрос для получения всех предметов преподавателя:**
```sql
SELECT t.full_name, s.subject_name, ta.academic_year, ta.semester
FROM teachers t
JOIN teaching_assignments ta ON t.teacher_id = ta.teacher_id
JOIN subjects s ON ta.subject_id = s.subject_id
WHERE t.teacher_id = ?;
```

---

## Ограничения и правила целостности

### Ограничения типа данных (Domain Constraints)

| Таблица | Поле | Ограничение | Причина |
|---------|------|-----------|---------|
| STUDENTS | student_id | AUTO_INCREMENT | Уникальное назначение ID |
| STUDENTS | full_name | NOT NULL | Обязательные данные |
| STUDENTS | birth_date | NOT NULL | Обязательные данные |
| STUDENTS | email | VARCHAR(50), NULL | Опциональное поле |
| TEACHERS | teacher_id | AUTO_INCREMENT | Уникальное назначение ID |
| SUBJECTS | category | CHECK (...) | Только допустимые категории |
| ENROLLMENTS | semester | CHECK (1 или 2) | Только 1 или 2 семестр |
| GRADES | grade | CHECK (1-5) | Диапазон оценок |

### Ограничения на сущности (Entity Integrity Constraints)

1. **Primary Keys:** Каждая таблица имеет PRIMARY KEY
   - Гарантирует уникальность каждой записи
   - Позволяет однозначно идентифицировать сущность

2. **Примеры:**
   ```sql
   PRIMARY KEY (student_id)
   PRIMARY KEY (teacher_id)
   PRIMARY KEY (subject_id)
   PRIMARY KEY (enrollment_id)
   PRIMARY KEY (grade_id)
   PRIMARY KEY (assignment_id)
   ```

### Ограничения на ссылочную целостность (Referential Integrity Constraints)

1. **Foreign Keys с ON DELETE CASCADE:**
   ```sql
   -- Если студент удаляется, удаляются его записи
   FOREIGN KEY (student_id) REFERENCES students(student_id) 
   ON DELETE CASCADE
   
   -- Если предмет удаляется, удаляются связанные данные
   FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) 
   ON DELETE CASCADE
   
   -- Если преподаватель удаляется, удаляются его оценки и назначения
   FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) 
   ON DELETE CASCADE
   ```

2. **Смысл:** Автоматическое поддержание целостности при удалении данных

### Уникальные ограничения (Uniqueness Constraints)

1. **ENROLLMENTS:**
   ```sql
   UNIQUE KEY uk_enrollments (student_id, subject_id, academic_year, semester)
   ```
   **Правило:** Студент не может быть записан дважды на один предмет в одном семестре

2. **TEACHING_ASSIGNMENTS:**
   ```sql
   UNIQUE KEY uk_teaching (teacher_id, subject_id, academic_year, semester)
   ```
   **Правило:** Преподаватель не может быть назначен дважды на один предмет в одном семестре

### Валидация данных (Check Constraints)

1. **Email validation:**
   ```sql
   CHECK ((email like '%@%') or (email is null))
   ```
   Email должен содержать '@' или быть NULL

2. **Категория предмета:**
   ```sql
   CHECK (category in ('Математические','Гуманитарные','Естественные','Прочие'))
   ```
   Только 4 допустимые категории (в имеющихся данных используются: Математические, Гуманитарные)

3. **Диапазон оценок:**
   ```sql
   CHECK (grade between 1 and 5)
   ```
   Оценки только от 1 до 5

4. **Номер семестра:**
   ```sql
   CHECK (semester in (1,2))
   ```
   Только 1 или 2 семестр

---
