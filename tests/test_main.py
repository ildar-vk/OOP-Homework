import os
import subprocess
import sys

import pytest


def test_main_execution() -> None:
    """Тест что main.py"""

    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "main.py"),
        os.path.join(os.path.dirname(__file__), "..", "..", "main.py"),
        "main.py",
    ]

    main_path = None
    for path in possible_paths:
        if os.path.exists(path):
            main_path = path
            break

    # Если файл не найден, пропускаем тест
    if main_path is None:
        pytest.skip("main.py not found")
        return

    # Выполняем main.py
    result = subprocess.run(
        [sys.executable, main_path],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(main_path),
        timeout=10,
    )

    # Проверяем что выполнение завершилось успешно
    assert result.returncode == 0, f"main.py failed:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"

    # Проверяем что есть какой-то вывод
    assert len(result.stdout) > 0, "main.py produced no output"


def test_main_content() -> None:
    """Тест что main.py содержит ожидаемый код"""
    # Пробуем разные возможные пути
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "main.py"),
        os.path.join(os.path.dirname(__file__), "..", "..", "main.py"),
        "main.py",
    ]

    main_path = None
    for path in possible_paths:
        if os.path.exists(path):
            main_path = path
            break

    # Если файл не найден, пропускаем тест
    if main_path is None:
        pytest.skip("main.py not found")
        return

    with open(main_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Проверяем ключевые элементы
    assert 'if __name__ == "__main__":' in content
    assert "Product(" in content
    assert "Category(" in content
