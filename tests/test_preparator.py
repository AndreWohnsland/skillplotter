from skill_plotter.preparator import reduce_data, sort_skills_by_category, split_dict_evenly


def test_split_dict_evenly():
    d = {"a": 1, "b": 2, "c": 3}
    chunks = split_dict_evenly(d, 2)
    assert len(chunks) == 2
    assert chunks[0] == {"a": 1, "b": 2}
    # uneven split pads the shorter chunk with an empty placeholder
    assert chunks[1] == {"c": 3, "": 0}


def test_sort_skills_by_category():
    skills = {
        "Vim": {"level": 5, "category": "tools"},
        "Python": {"level": 9, "category": "default"},
        "Docker": {"level": 7, "category": "tools"},
    }
    # default category first, then by category and descending level
    assert list(sort_skills_by_category(skills)) == ["Python", "Docker", "Vim"]


def test_reduce_data():
    skills = {"Python": {"level": 9, "category": "default"}}
    assert reduce_data(skills) == {"Python": 9}
