#include "func.hpp"
#include <zeno/NumericObject.h>
#include <zeno/zeno.h>

namespace your_namespace {

struct your_add_node : zeno::INode {
  void apply() override {
    using namespace zeno;
    float num1 = get_input("num1")->as<NumericObject>()->get<float>();
    float num2 = get_input("num2")->as<NumericObject>()->get<float>();
    auto result = IObject::make<NumericObject>();
    auto sum = compute_sum({num1, num2});
    result->set<float>(sum);
    set_output("result", result);
  }
};

ZENDEFNODE(your_add_node, {
                              {"num1", "num2"},
                              {"result"},
                              {},
                              {"YourNodeSeries"},
                          });

} // namespace your_namespace