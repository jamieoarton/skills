# Update Space

Rename, set the Space color, and enable ClickApps for a Space.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/space/{space_id}": {
      "put": {
        "summary": "Update Space",
        "tags": [
          "Spaces"
        ],
        "description": "Rename, set the Space color, and enable ClickApps for a Space.",
        "operationId": "UpdateSpace",
        "parameters": [
          {
            "name": "space_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                790
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateSpacerequest",
                "required": [
                  "name",
                  "color",
                  "private",
                  "admin_can_manage",
                  "multiple_assignees",
                  "features"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "color": {
                    "type": "string"
                  },
                  "private": {
                    "type": "boolean"
                  },
                  "admin_can_manage": {
                    "description": "***Note:** Allowing or restricting admins from managing private Spaces using `\"admin_can_manage\"` is an [Enterprise Plan](https://clickup.com/pricing) feature.*",
                    "type": "boolean"
                  },
                  "multiple_assignees": {
                    "type": "boolean"
                  },
                  "features": {
                    "title": "Features",
                    "required": [
                      "due_dates",
                      "time_tracking",
                      "tags",
                      "time_estimates",
                      "checklists",
                      "custom_fields",
                      "remap_dependencies",
                      "dependency_warning",
                      "portfolios"
                    ],
                    "type": "object",
                    "properties": {
                      "due_dates": {
                        "title": "DueDates",
                        "required": [
                          "enabled",
                          "start_date",
                          "remap_due_dates",
                          "remap_closed_due_date"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          },
                          "start_date": {
                            "type": "boolean"
                          },
                          "remap_due_dates": {
                            "type": "boolean"
                          },
                          "remap_closed_due_date": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true,
                            "start_date": false,
                            "remap_due_dates": true,
                            "remap_closed_due_date": false
                          }
                        ]
                      },
                      "time_tracking": {
                        "title": "TimeTracking",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": false
                          }
                        ]
                      },
                      "tags": {
                        "title": "Tags",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "time_estimates": {
                        "title": "TimeEstimates",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "checklists": {
                        "title": "Checklists",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "custom_fields": {
                        "title": "CustomFields",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "remap_dependencies": {
                        "title": "RemapDependencies",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "dependency_warning": {
                        "title": "DependencyWarning",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      },
                      "portfolios": {
                        "title": "Portfolios",
                        "required": [
                          "enabled"
                        ],
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "enabled": true
                          }
                        ]
                      }
                    },
                    "examples": [
                      {
                        "due_dates": {
                          "enabled": true,
                          "start_date": false,
                          "remap_due_dates": true,
                          "remap_closed_due_date": false
                        },
                        "time_tracking": {
                          "enabled": false
                        },
                        "tags": {
                          "enabled": true
                        },
                        "time_estimates": {
                          "enabled": true
                        },
                        "checklists": {
                          "enabled": true
                        },
                        "custom_fields": {
                          "enabled": true
                        },
                        "remap_dependencies": {
                          "enabled": true
                        },
                        "dependency_warning": {
                          "enabled": true
                        },
                        "portfolios": {
                          "enabled": true
                        }
                      }
                    ]
                  }
                },
                "examples": [
                  {
                    "name": "Updated Space Name",
                    "color": "#7B68EE",
                    "private": false,
                    "admin_can_manage": false,
                    "multiple_assignees": false,
                    "features": {
                      "due_dates": {
                        "enabled": false,
                        "start_date": false,
                        "remap_due_dates": false,
                        "remap_closed_due_date": false
                      },
                      "time_tracking": {
                        "enabled": false
                      },
                      "tags": {
                        "enabled": false
                      },
                      "time_estimates": {
                        "enabled": false
                      },
                      "checklists": {
                        "enabled": true
                      },
                      "custom_fields": {
                        "enabled": true
                      },
                      "remap_dependencies": {
                        "enabled": false
                      },
                      "dependency_warning": {
                        "enabled": false
                      },
                      "portfolios": {
                        "enabled": false
                      }
                    }
                  }
                ]
              },
              "example": {
                "name": "Updated Space Name",
                "color": "#7B68EE",
                "private": false,
                "admin_can_manage": false,
                "multiple_assignees": false,
                "features": {
                  "due_dates": {
                    "enabled": false,
                    "start_date": false,
                    "remap_due_dates": false,
                    "remap_closed_due_date": false
                  },
                  "time_tracking": {
                    "enabled": false
                  },
                  "tags": {
                    "enabled": false
                  },
                  "time_estimates": {
                    "enabled": false
                  },
                  "checklists": {
                    "enabled": true
                  },
                  "custom_fields": {
                    "enabled": true
                  },
                  "remap_dependencies": {
                    "enabled": false
                  },
                  "dependency_warning": {
                    "enabled": false
                  },
                  "portfolios": {
                    "enabled": false
                  }
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "UpdateSpaceresponse",
                  "required": [
                    "id",
                    "name",
                    "private",
                    "statuses",
                    "multiple_assignees",
                    "features"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "private": {
                      "type": "boolean"
                    },
                    "statuses": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                      },
                      "description": ""
                    },
                    "multiple_assignees": {
                      "type": "boolean"
                    },
                    "features": {
                      "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features"
                    }
                  },
                  "examples": [
                    {
                      "id": "790",
                      "name": "Updated Space Name",
                      "private": false,
                      "statuses": [
                        {
                          "status": "to do",
                          "type": "open",
                          "orderindex": 0,
                          "color": "#d3d3d3"
                        },
                        {
                          "status": "complete",
                          "type": "closed",
                          "orderindex": 1,
                          "color": "#6bc950"
                        }
                      ],
                      "multiple_assignees": false,
                      "features": {
                        "due_dates": {
                          "enabled": false,
                          "start_date": false,
                          "remap_due_dates": false,
                          "remap_closed_due_date": false
                        },
                        "time_tracking": {
                          "enabled": false
                        },
                        "tags": {
                          "enabled": false
                        },
                        "time_estimates": {
                          "enabled": false
                        },
                        "checklists": {
                          "enabled": true
                        },
                        "custom_fields": {
                          "enabled": true
                        },
                        "remap_dependencies": {
                          "enabled": false
                        },
                        "dependency_warning": {
                          "enabled": false
                        },
                        "portfolios": {
                          "enabled": false
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "id": "790",
                  "name": "Updated Space Name",
                  "private": false,
                  "statuses": [
                    {
                      "status": "to do",
                      "type": "open",
                      "orderindex": 0,
                      "color": "#d3d3d3"
                    },
                    {
                      "status": "complete",
                      "type": "closed",
                      "orderindex": 1,
                      "color": "#6bc950"
                    }
                  ],
                  "multiple_assignees": false,
                  "features": {
                    "due_dates": {
                      "enabled": false,
                      "start_date": false,
                      "remap_due_dates": false,
                      "remap_closed_due_date": false
                    },
                    "time_tracking": {
                      "enabled": false
                    },
                    "tags": {
                      "enabled": false
                    },
                    "time_estimates": {
                      "enabled": false
                    },
                    "checklists": {
                      "enabled": true
                    },
                    "custom_fields": {
                      "enabled": true
                    },
                    "remap_dependencies": {
                      "enabled": false
                    },
                    "dependency_warning": {
                      "enabled": false
                    },
                    "portfolios": {
                      "enabled": false
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Spaces"
    }
  ]
}
```