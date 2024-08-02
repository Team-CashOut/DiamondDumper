from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Set, List, Optional
from re import Pattern



@dataclass
class AdminRight:
    is_group: bool
    subs: int
    title: str

    def __str__(self) -> str:
        entity_type = 'Group' if self.is_group else 'Channel'
        return f'{entity_type} "{self.title}", {self.subs} subs'


@dataclass(frozen=True)
class BotBalance:
    bot: Bot
    balance: Optional[str]

    def __str__(self) -> str:
        balance = self.balance if self.balance is not None else 'not found'
        return f'{self.bot.peer} - {balance}'


@dataclass
class Result:
    path: str
    is_valid: bool = field(default=False)
    phone: Optional[str] = field(default=None)
    seeds: Set = field(default_factory=set)
    admin_rights: List[AdminRight] = field(default_factory=list)
    bots: Dict[Bot, BotBalance] = field(default_factory=dict)


@dataclass(frozen=True)
class Bot:
    peer: str
    regex: Pattern

    def check(self, text: str) -> str:
        res = self.regex.search(text)
        if res:
            res = res.group(1)
        return res