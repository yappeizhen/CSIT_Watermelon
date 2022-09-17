def test_to_cumulative_with_single_tick(self):
  self.assertEqual([
      "00:00,A,5,27.5",
  ], to_cumulative([
      "00:00,A,5,5.5",
  ]))


def test_to_cumulative_with_multiple_ticks_for_different_tickers(self):
  self.assertEqual([
      "00:00,A,5,27.5,B,4,17.6",
  ], to_cumulative([
      "00:00,B,4,4.4",
      "00:00,A,5,5.5",
  ]))


def test_to_cumulative_delayed(self):
  self.assertEqual([
      "00:05,A,5,28.0",
  ], to_cumulative_delayed([
      "00:05,A,1,5.6",
      "00:00,A,1,5.6",
      "00:02,A,1,5.6",
      "00:03,A,1,5.6",
      "00:04,A,1,5.6",
  ], 5))# Enter code here


def test_to_cumulative_delayed_with_different_tickers(self):
  self.assertEqual([
      "00:00,B,5,27.5",
      "00:01,A,5,27.9",
  ], to_cumulative_delayed([
      "00:01,A,5,5.5",
      "00:00,A,4,5.6",
      "00:00,B,5,5.5",
      "00:02,B,4,5.6",
  ], 5))



