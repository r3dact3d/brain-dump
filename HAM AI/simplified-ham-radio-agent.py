from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
import feedparser
import json
import logging
from pathlib import Path

@dataclass
class RadioEvent:
    timestamp: datetime
    event_type: str
    title: str
    description: str
    priority: int
    source: str

class DataCollector:
    """Handles data collection from RSS feeds and local files"""
    def __init__(self, feed_urls: List[str], data_directory: Path):
        self.feed_urls = feed_urls
        self.data_directory = data_directory

    def collect_rss_data(self) -> List[RadioEvent]:
        events = []
        for url in self.feed_urls:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    events.append(RadioEvent(
                        timestamp=datetime.now(),
                        event_type="news",
                        title=entry.title,
                        description=entry.description,
                        priority=3,
                        source=url
                    ))
            except Exception as e:
                logging.error(f"Error collecting RSS data from {url}: {e}")
        return events

class Analyzer:
    """Processes and categorizes radio events"""
    def analyze_events(self, events: List[RadioEvent]) -> List[RadioEvent]:
        analyzed_events = []
        for event in events:
            # Analyze event content and adjust priority
            if any(keyword in event.description.lower() 
                  for keyword in ['emergency', 'urgent', 'alert']):
                event.priority = 1
            analyzed_events.append(event)
        return analyzed_events

class KnowledgeBase:
    """Maintains amateur radio information and regulations"""
    def __init__(self, data_file: Path):
        self.data_file = data_file
        self.knowledge = self._load_knowledge()

    def _load_knowledge(self) -> Dict:
        try:
            return json.loads(self.data_file.read_text())
        except Exception:
            return {}

    def enrich_event(self, event: RadioEvent) -> RadioEvent:
        # Add relevant knowledge base information to event
        if related_info := self.knowledge.get(event.event_type):
            event.description += f"\n\nRelated Information: {related_info}"
        return event

class ReportGenerator:
    """Generates formatted markdown reports"""
    def generate_report(self, events: List[RadioEvent]) -> str:
        report = ["# Amateur Radio Net Report\n"]
        report.append(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}")
        report.append(f"**Time**: {datetime.now().strftime('%H:%M')} UTC\n")

        # Group events by priority
        priority_events = [e for e in events if e.priority == 1]
        if priority_events:
            report.append("## Emergency Communications")
            for event in priority_events:
                report.append(f"- **{event.title}**\n  {event.description}\n")

        # Add regular events
        report.append("## News and Updates")
        for event in [e for e in events if e.priority > 1]:
            report.append(f"- **{event.title}**\n  {event.description}\n")

        return "\n".join(report)

class HamRadioAgent:
    """Main coordinator class that manages the entire process"""
    def __init__(self, config_file: Path):
        config = json.loads(config_file.read_text())
        self.data_collector = DataCollector(
            config['feed_urls'],
            Path(config['data_directory'])
        )
        self.analyzer = Analyzer()
        self.knowledge_base = KnowledgeBase(Path(config['knowledge_file']))
        self.report_generator = ReportGenerator()

    def process_and_report(self) -> str:
        # Collect data
        events = self.data_collector.collect_rss_data()
        
        # Analyze and prioritize
        events = self.analyzer.analyze_events(events)
        
        # Enrich with knowledge base information
        events = [self.knowledge_base.enrich_event(event) for event in events]
        
        # Generate report
        return self.report_generator.generate_report(events)

def main():
    agent = HamRadioAgent(Path("config.json"))
    report = agent.process_and_report()
    print(report)

if __name__ == "__main__":
    main()
