import unittest
from pathlib import Path


class ReadmeStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = Path("README.md").read_text(encoding="utf-8")

    def test_required_sections_exist(self):
        required_sections = [
            "## 👋 Hello, I'm Rohit",
            "## 🧠 Professional Snapshot",
            "## 🛠️ Tech I Have Worked With",
            "## 🚀 Use Cases & Outcomes",
            "## 📫 Let’s Connect",
        ]
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, self.readme)

    def test_core_technologies_and_tooling_are_listed(self):
        technologies = [
            "C#/.NET",
            "React",
            "Node.js",
            "Express",
            "Python",
            "MySQL",
            "PostgreSQL",
            "Blockchain",
            "OpenVINO",
            "Antigravity",
            "OpenAI Codex",
            "OpenCLAW",
            "ChatGPT",
            "Gemini",
            "Claude",
        ]
        for tech in technologies:
            with self.subTest(tech=tech):
                self.assertIn(tech, self.readme)

    def test_featured_projects_section_removed(self):
        self.assertNotIn("## 🌟 Featured Projects", self.readme)


if __name__ == "__main__":
    unittest.main()
