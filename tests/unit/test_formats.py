"""Tests for format-specific parsers."""

from __future__ import annotations

import pytest

from ftdata.core.formats import parse_alpaca, parse_chatml, parse_sharegpt


class TestParseChatML:
    @pytest.mark.skip(reason="Format parsers not yet implemented")
    def test_parse_basic(self) -> None:
        raw = {
            "messages": [
                {"role": "user", "content": "Hi"},
                {"role": "assistant", "content": "Hello!"},
            ]
        }
        sample = parse_chatml(raw, index=0)
        assert sample.turn_count == 2

    @pytest.mark.skip(reason="Format parsers not yet implemented")
    def test_parse_with_system(self) -> None:
        raw = {
            "messages": [
                {"role": "system", "content": "You are helpful."},
                {"role": "user", "content": "Hi"},
                {"role": "assistant", "content": "Hello!"},
            ]
        }
        sample = parse_chatml(raw, index=0)
        assert sample.has_system is True


class TestParseAlpaca:
    @pytest.mark.skip(reason="Format parsers not yet implemented")
    def test_parse_with_input(self) -> None:
        raw = {"instruction": "Summarize", "input": "Some text.", "output": "Summary."}
        sample = parse_alpaca(raw, index=0)
        assert sample.turn_count > 0

    @pytest.mark.skip(reason="Format parsers not yet implemented")
    def test_parse_without_input(self) -> None:
        raw = {"instruction": "Write a haiku.", "input": "", "output": "A haiku here."}
        sample = parse_alpaca(raw, index=0)
        assert sample.turn_count > 0


class TestParseShareGPT:
    @pytest.mark.skip(reason="Format parsers not yet implemented")
    def test_parse_basic(self) -> None:
        raw = {
            "conversations": [{"from": "human", "value": "Hi"}, {"from": "gpt", "value": "Hello!"}]
        }
        sample = parse_sharegpt(raw, index=0)
        assert sample.turn_count == 2
