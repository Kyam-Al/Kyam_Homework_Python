from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:postgres@localhost:5432/Квест"


def test_insert():
    engine = create_engine(DB_URL)

    with engine.begin() as connection:
        # insert
        connection.execute(
            text(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (1001, 'Geometry')"
            )
        )

        # select
        result = connection.execute(
            text(
                "SELECT subject_id, subject_title "
                "FROM subject WHERE subject_id = 1001"
            )
        )

        subject_id, subject_title = result.fetchone()
        assert subject_id == 1001
        assert subject_title == "Geometry"

        # cleanup
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = 1001")
        )


def test_update():
    engine = create_engine(DB_URL)

    with engine.begin() as connection:
        # prepare data
        connection.execute(
        text(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (1002, 'Temp')"
            )
        )

        # update
        connection.execute(
            text(
                "UPDATE subject "
                "SET subject_title = 'Physics' "
                "WHERE subject_id = 1002"
            )
        )

        # select
        result = connection.execute(
            text(
                "SELECT subject_id, subject_title "
                "FROM subject WHERE subject_id = 1002"
            )
        )

        subject_id, subject_title = result.fetchone()
        assert subject_id == 1002
        assert subject_title == "Physics"

        # cleanup
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = 1002")
        )


def test_delete():
    engine = create_engine(DB_URL)

    with engine.begin() as connection:
        # prepare data
        connection.execute(
            text(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (1003, 'Biology')"
            )
        )

        # delete
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = 1003")
        )

        # select
        result = connection.execute(
            text(
                "SELECT * FROM subject WHERE subject_id = 1003"
            )
        )

        assert result.fetchall() == []